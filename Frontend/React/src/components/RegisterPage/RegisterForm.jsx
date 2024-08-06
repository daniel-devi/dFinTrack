import { TextField, Grid, Button, Typography, Link, Box } from "@mui/material";

// Component for the registration form
const RegisterForm = ({ handleSubmit, error }) => {
  return (
    <Box
      component="form"
      validate="true"
      onSubmit={handleSubmit}
      sx={{ mt: 3 }}
    >
      <link rel="preconnect" href="https://fonts.googleapis.com" />
      <link rel="preconnect" href="https://fonts.gstatic.com" crossOrigin="" />
      <link
        href="https://fonts.googleapis.com/css2?family=Doppio+One&family=Inconsolata:wght@200..900&display=swap"
        rel="stylesheet"
      />
      <Typography variant="h6" sx={{ mb: 4 }} color={"blue"}>
        Be in Control of your Finances
      </Typography>
      <Grid container spacing={2}>
        <Grid item xs={12} sm={6}>
          <TextField
            autoComplete="given-name"
            name="firstName"
            required
            fullWidth
            id="firstName"
            label="First Name"
            placeholder="John"
            autoFocus
          />
        </Grid>
        <Grid item xs={12} sm={6}>
          <TextField
            fullWidth
            id="lastName"
            label="Last Name"
            name="lastName"
            autoComplete="family-name"
            placeholder="Calver"
          />
        </Grid>
        <Grid item xs={12}>
          <TextField
            required
            fullWidth
            id="Email"
            label="Email"
            name="Email"
            autoComplete="email"
            placeholder="someone@example.com"
          />
        </Grid>
        <Grid item xs={12}>
          <TextField
            required
            fullWidth
            name="password"
            label="Password"
            type="password"
            id="password"
            autoComplete="new-password"
          />
        </Grid>
        <Grid item xs={12}>
          {/** TODO: ADD THIRD-PARTY AUTHENTICATION */}
        </Grid>
      </Grid>
      <Button type="submit" fullWidth variant="contained" sx={{ mt: 3, mb: 2 }}>
        Sign Up
      </Button>
      <Typography>{error}</Typography> {/* Display any error messages */}
      <Grid container justifyContent="flex-end">
        <Grid item>
          <Link href="login" variant="body2">
            Already have an account? Sign in
          </Link>
        </Grid>
      </Grid>
    </Box>
  );
};

export default RegisterForm;
