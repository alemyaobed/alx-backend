import kue from 'kue';

// Create a queue with Kue
const queue = kue.createQueue();

// Create an object containing the Job data
const jobData = {
  phoneNumber: '1234567890',
  message: 'This is a test message',
};

// Create a queue named push_notification_code, and create a job with the object created before
const job = queue.create('push_notification_code', jobData)
  .save((err) => {
    if (!err) console.log(`Notification job created: ${job.id}`);
  });

// When the job is completed, log to the console Notification job completed
job.on('complete', () => {
    console.log('Notification job completed');
  });

// When the job is failing, log to the console Notification job failed
job.on('failed', () => {
    console.log('Notification job failed');
  });
