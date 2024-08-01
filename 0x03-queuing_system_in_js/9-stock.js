import { createClient } from 'redis';
import express from 'express';
import { promisify } from 'util';

const app = express();
const port = 1245;

// Create a Redis client
const client = createClient();

client.on('error', (err) => console.error('Redis Client Error', err));



// Promisify the Redis client methods
const getAsync = promisify(client.get).bind(client);

// Sample product data
const listProducts = [
  { id: 1, name: 'Suitcase 250', price: 50, stock: 4 },
  { id: 2, name: 'Suitcase 450', price: 100, stock: 10 },
  { id: 3, name: 'Suitcase 650', price: 350, stock: 2 },
  { id: 4, name: 'Suitcase 1050', price: 550, stock: 5 },
];

// Function to get product by ID
const getItemById = (id) => listProducts.find((product) => product.id === id);

// Route to list all products
app.get('/list_products', (req, res) => {
  const productsResponse = listProducts.map(({ id, name, price, stock }) => ({
    itemId: id,
    itemName: name,
    price,
    initialAvailableQuantity: stock,
  }));
  res.json(productsResponse);
});

// Function to reserve stock by ID
const reserveStockById = async (itemId, stock) => {
  const key = `item.${itemId}`
  await client.set(key, stock);
};

// Function to get current reserved stock by ID
const getCurrentReservedStockById = async (itemId) => {
  const reservedStock = await getAsync(`item.${itemId}`);
  return reservedStock ? parseInt(reservedStock, 10) : 0;
};

// Route to get product details by ID
app.get('/list_products/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId, 10);
  const product = getItemById(itemId);

  if (!product) {
    return res.json({ status: 'Product not found' });
  }

  const currentQuantity = await getCurrentReservedStockById(itemId);
  res.json({
    itemId: product.id,
    itemName: product.name,
    price: product.price,
    initialAvailableQuantity: product.stock,
    currentQuantity: product.stock - currentQuantity,
  });
});

// Route to reserve a product
app.get('/reserve_product/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId, 10);
  const product = getItemById(itemId);

  if (!product) {
    return res.json({ status: 'Product not found' });
  }

  const currentQuantity = await getCurrentReservedStockById(itemId);
  if (currentQuantity >= product.stock) {
    return res.json({
      status: 'Not enough stock available',
      itemId: product.id,
    });
  }

  await reserveStockById(itemId, currentQuantity + 1);
  res.json({
    status: 'Reservation confirmed',
    itemId: product.id,
  });
});

// Start the server
app.listen(port, () => {
  console.log(`Server listening on port ${port}`);
});
