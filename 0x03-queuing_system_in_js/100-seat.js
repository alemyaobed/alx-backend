import express from 'express';
import { createClient } from 'redis';
import kue from 'kue';
import { promisify } from 'util';

// Create a Redis client
const client = createClient();

// Handle connection events
client.on('connect', () => {
    console.log('Redis client connected to the server');
});
client.on('error', (error) => {
    console.log(`Redis client not connected to the server: ${error.message}`);
});

// Promisify Redis client methods
const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

// Initialize the number of available seats
const INITIAL_AVAILABLE_SEATS = 50;

// Set initial available seats
setAsync('available_seats', INITIAL_AVAILABLE_SEATS);

// Initialize reservation status
let reservationEnabled = true;

// Create a Kue queue
const queue = kue.createQueue();

// Create an Express server
const app = express();

// Route to get available seats
app.get('/available_seats', async (req, res) => {
  const availableSeats = await getAsync('available_seats');
  res.json({ numberOfAvailableSeats: availableSeats });
});

// Route to reserve a seat
app.get('/reserve_seat', (req, res) => {
  if (!reservationEnabled) {
    return res.json({ status: 'Reservation are blocked' });
  }

  const job = queue.create('reserve_seat').save((err) => {
    if (err) {
      return res.json({ status: 'Reservation failed' });
    }
    res.json({ status: 'Reservation in process' });
  });

  job.on('complete', () => {
    console.log(`Seat reservation job ${job.id} completed`);
  });

  job.on('failed', (error) => {
    console.log(`Seat reservation job ${job.id} failed: ${error}`);
  });
});

// Route to process the queue
app.get('/process', (req, res) => {
  res.json({ status: 'Queue processing' });
  queue.process('reserve_seat', async (job, done) => {
    const availableSeats = await getAsync('available_seats');
    const newAvailableSeats = parseInt(availableSeats, 10) - 1;

    await setAsync('available_seats', newAvailableSeats);

    if (newAvailableSeats === 0) {
      reservationEnabled = false;
    }

    if (newAvailableSeats >= 0) {
      done(); // Job succeeded
    } else {
      done(new Error('Not enough seats available')); // Job failed
    }
  });
});

// Start the Express server
app.listen(1245, () => {
  console.log('Server is running on port 1245');
});
