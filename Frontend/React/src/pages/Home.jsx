import React from 'react';
import { AppBar, Toolbar, Typography, Container, Box, Button } from '@mui/material';

function HomePage() {
  return (
    <div>
      {/* Navigation Bar */}
      <AppBar position="static">
        <Toolbar>
          <Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>
            My Website
          </Typography>
          <Button color="inherit" href="/dashboard">Dashboard</Button>
          <Button color="inherit" href="/login">Login</Button>
          <Button color="inherit" href="/register">Register</Button>
        </Toolbar>
      </AppBar>

      {/* Main Content */}
      <Container maxWidth="md">
        <Box sx={{ my: 4 }}>
          <Typography variant="h3" component="h1" gutterBottom>
            Welcome to My Website
          </Typography>
          <Typography variant="h5" component="h2" gutterBottom>
            This is a simple homepage created with React and Material UI.
          </Typography>
          <Typography variant="body1" gutterBottom>
            Explore the features and enjoy your stay!
          </Typography>
        </Box>
      </Container>
    </div>
  );
}

export default HomePage;
