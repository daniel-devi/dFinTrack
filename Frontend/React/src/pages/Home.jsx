import { Typography, Container, Box } from '@mui/material';
import NavBar from '../components/AppNavBar';

function HomePage() {
  return (
    <div>
      {/* Navigation Bar */}
      <NavBar/>

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
