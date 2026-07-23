# ==========================================
# Stage 1: Build the React application
# ==========================================
FROM node:20-alpine AS build

# Set the working directory inside the container
WORKDIR /app

# Copy dependency definitions first to leverage Docker layer caching
COPY package.json package-lock.json* ./

# Install dependencies
RUN npm install

# Copy all the source code to the container
COPY . .

# Build the React application for production
# (If you are using Create React App instead of Vite, change 'dist' to 'build' in the next stage)
RUN npm run build

# ==========================================
# Stage 2: Serve the application with Nginx
# ==========================================
FROM nginx:alpine

# Copy the compiled static files from the build stage to Nginx's serve directory
COPY --from=build /app/dist /usr/share/nginx/html

# Copy the custom Nginx configuration to handle React Router 404s
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Expose port 80 to the Docker network
EXPOSE 80

# Start the Nginx server
CMD ["nginx", "-g", "daemon off;"]
