
import { createClient } from 'redis'
import redis from 'redis';

// Create a Redis client
const client = createClient();

// Handle connection events
client.on('connect', () => {
  console.log('Redis client connected to the server');
});
client.on('error', (error) => {
  console.log(`Redis client not connected to the server: ${error.message}`);
});

// Function to set hash values
function createHash() {
  client.hset('HolbertonSchools', 'Portland', 50, redis.print);
  client.hset('HolbertonSchools', 'Seattle', 80, redis.print);
  client.hset('HolbertonSchools', 'New York', 20, redis.print);
  client.hset('HolbertonSchools', 'Bogota', 20, redis.print);
  client.hset('HolbertonSchools', 'Cali', 40, redis.print);
  client.hset('HolbertonSchools', 'Paris', 2, redis.print);
}

// Function to display hash values
function displayHash() {
  client.hgetall('HolbertonSchools', (err, obj) => {
    if (err) {
      console.error(err);
    } else {
      console.log(obj);
    }
  });
}

// Create and display the hash
createHash();
displayHash();