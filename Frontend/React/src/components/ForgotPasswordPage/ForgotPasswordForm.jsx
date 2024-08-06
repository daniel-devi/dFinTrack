import { useState, useEffect} from 'react';
import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';
import Grid from '@mui/material/Grid';
import Box from '@mui/material/Box';

// SignInForm component for handling the sign-in form
export default function ForgotPasswordForm() {
  // State for managing form errors
  const [error, setError] = useState(false);
  const [errorMessageUsername, setErrorMessageUsername] = useState("");

  // Handle form submission
  const handleSubmit = (event) => {
    event.preventDefault();
    const data = new FormData(event.currentTarget);

    // Log form data to the console
    console.log({
      email: data.get('email'),
      password: data.get('password'),
    });

    // Add form submission logic here
  };

  return (
    <Box component="form" onSubmit={handleSubmit} noValidate sx={{ mt: 1 }}>
      {/* Email input field */}
      <TextField
        margin="normal"
        required
        fullWidth
        id="email"
        label="Email Address"
        name="email"
        autoComplete="email"
        autoFocus
        error={error}
        helperText={errorMessageUsername}
      />

      {/* Forget Password button */}
      <Button
        type="submit"
        fullWidth
        variant="contained"
        sx={{ mt: 3, mb: 2 }}
      >
        Send me Password Reset Link
      </Button>
    </Box>
  );
}
