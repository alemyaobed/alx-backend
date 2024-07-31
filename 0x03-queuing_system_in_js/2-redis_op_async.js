import { createClient } from 'redis';
import { promisify } from 'util';

// Create a Redis client
const client = createClient();

// Handle connection events
client.on('connect', () => {console.log('Redis client connected to the server')});
client.on('error', (error) => {console.log(`Redis client not connected to the server: ${error.message}`)});

// Promisify the get method
const getAsync = promisify(client.get).bind(client);

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

// Asynchronous function to display school value
async function displaySchoolValue(schoolName) {
  try {
    const value = await getAsync(schoolName);
    console.log(value); // Log the value to the console
  } catch (err) {
    console.error('Error getting value:', err);
  }
}

// Executing functions
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
