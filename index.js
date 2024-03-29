const jsonServer = require("json-server"); // importing json-server library
const server = jsonServer.create();
const router = jsonServer.router("db.json");
const middlewares = jsonServer.defaults();
const customMiddleware = require('./CustomMiddleware');
const port = process.env.PORT || 8080; //  chose port from here like 8080, 3001

server.use(customMiddleware);
server.use(middlewares);
server.use(router);

server.listen(port);