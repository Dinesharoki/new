# Use a Java base image
FROM openjdk:17-jdk-slim

# Set working directory
WORKDIR /app

# Copy JAR file into the container
COPY target/hello-world-1.0-SNAPSHOT.jar hello-world.jar

# Set the command to run the app
CMD ["java", "-jar", "hello-world.jar"]

