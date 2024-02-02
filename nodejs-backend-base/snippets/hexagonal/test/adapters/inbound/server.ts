import { createServer } from "http";

const server = createServer();

server.listen(3000, () => console.log("Server is up and running!"));
