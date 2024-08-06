import { createTheme, ThemeProvider } from '@mui/material/styles';
import Container from '@mui/material/Container';
import CssBaseline from '@mui/material/CssBaseline';
import Box from '@mui/material/Box';
import Avatar from '@mui/material/Avatar';
import Typography from '@mui/material/Typography';
import ForgotPasswordForm from './ForgotPasswordForm'; // Import the ForgotPasswordForm component
import Copyright from '../Copyright'; // Import the Copyright component
import LockOutlinedIcon from '@mui/icons-material/LockOutlined';

// Default theme for Material-UI
const defaultTheme = createTheme();

// Main SignIn component
export default function ForgotPassword() {
  return (
    <ThemeProvider theme={defaultTheme}>
      <Container component="main" maxWidth="xs">
        <CssBaseline />
        <Box
          sx={{
            marginTop: 8,
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center',
          }}
        >
          {/* Avatar icon for the forgot password page */}
          <Avatar sx={{ m: 1, bgcolor: 'secondary.main' }}>
            <LockOutlinedIcon />
          </Avatar>

          {/* Forgot Password heading */}
          <Typography component="h1" variant="h5">
            Forgot My Password
          </Typography>

          {/* Forgot Password form */}
          <ForgotPassword />
        </Box>

        {/* Copyright footer */}
        <Copyright sx={{ mt: 8, mb: 4 }} />
      </Container>
    </ThemeProvider>
  );
}
