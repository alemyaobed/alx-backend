import { createClient } from 'redis';

// Create a Redis client
const client = createClient();

// Handle connection events
client.on('connect', () => {console.log('Redis client connected to the server')});
client.on('error', (error) => {console.log(`Redis client not connected to the server: ${error.message}`)});

// Function to set a new school value
function setNewSchool(schoolName, value) {
  client.set(schoolName, value, (err, reply) => {
    if (err) {
    console.error('Error setting value:', err);
    } else {
    console.log(`Reply: ${reply}`); // Display confirmation message
    }
  });
}

// Function to display the value of a school
function displaySchoolValue(schoolName) {
  client.get(schoolName, (err, value) => {
    if (err) {
      console.error('Error getting value:', err);
    } else {
      console.log(value); // Log the value to the console
    }
  });
}

// Executing functions
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
