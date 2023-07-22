// customMiddleware.js

const TOKEN = 'admin'; // Replace with your actual secret token

// Custom middleware function to handle authorization
const customMiddleware = (req, res, next) => {

  if (req.method !== 'GET') {
    const { authorization } = req.headers;
    if (!authorization || !authorization.startsWith('Bearer ')) {
      return res.status(401).json({ error: 'Unauthorized. Token not provided.' });
    }

    const token = authorization.split(' ')[1];

    if (token !== TOKEN) {
      return res.status(403).json({ error: 'Forbidden. Invalid token.' });
    }
  }
  // Token is valid, proceed to the next middleware or Json Server's default behavior
  next();
};

module.exports = customMiddleware;
