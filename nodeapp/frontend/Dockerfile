# Use Node.js 18 as the base image
FROM node:18

# Set the working directory
WORKDIR /app

# Copy package.json and package-lock.json to the working directory
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the app's files
COPY . .

# Expose the port your app will run on
EXPOSE 3000

# Set the entry point explicitly
CMD ["node", "app.js"]
