import { useState } from "react";
import Avatar from "@mui/material/Avatar";
import CssBaseline from "@mui/material/CssBaseline";
import Typography from "@mui/material/Typography";
import Container from "@mui/material/Container";
import { Box, Grid } from "@mui/material";
import { createTheme, ThemeProvider } from "@mui/material/styles";
import LockOutlinedIcon from "@mui/icons-material/LockOutlined";
import AlertMessage from "../AlertMessage";
import RegisterForm from "./RegisterForm";
import api from "../api";
import Copyright from "../Copyright";

// Define a default theme for Material UI components
const defaultTheme = createTheme();

export default function Register() {
  const [error, setError] = useState(""); // State to store error messages
  const [open, setOpen] = useState(false); // State to control the visibility of the success alert

  // Handle form submission
  const handleSubmit = async (event) => {
    event.preventDefault(); // Prevent the default form submission behavior
    const data = new FormData(event.currentTarget); // Get form data

    try {
      // Generate a unique username
      let userName =
        data.get("firstName") +
        data.get("lastName") +
        Math.floor(Math.random() * 10);

      // Make a POST request to register the user
      const res = await api.post("api/user/register/", {
        first_name: data.get("firstName"),
        username: userName,
        last_name: data.get("lastName"),
        email: data.get("Email"),
        password: data.get("password"),
      });

      if (res.status === 201) {
        setOpen(true); // Show success alert if registration is successful
        setTimeout(() => {
          window.location.href = "http://localhost:5173/login"; // Redirect to the login page after 3.5 seconds
        }, 3500);
      }
    } catch (error) {
      setError("An error occurred. Please try again later."); // Set error message if registration fails
    }
  };

  const BackgroundImage = () => (
    <Grid
      item
      xs={false}
      sm={4}
      md={7}
      sx={{
        backgroundImage:
          "url(https://th.bing.com/th/id/R.c1d6c5e5633d4287ff2002c3d1ab62f9?rik=rI%2fmmiVkVk55hQ&pid=ImgRaw&r=0)",
        backgroundRepeat: "no-repeat",
        backgroundColor: (t) =>
          t.palette.mode === "light" ? t.palette.grey[50] : t.palette.grey[900],
        backgroundSize: "cover",
        backgroundPosition: "center",
      }}
    />
  );

  return (
    <ThemeProvider theme={defaultTheme}>
      <Container component="main" maxWidth="xs">
        <CssBaseline />
        <BackgroundImage/>
        <Box
          sx={{
            marginTop: 8,
            display: "flex",
            flexDirection: "column",
            alignItems: "center",
          }}
        >
          {/* Show alert message if registration is successful */}
          <AlertMessage
            open={open}
            setOpen={setOpen}
            message="Account Successfully Created"
          />

          <Avatar sx={{ m: 1, bgcolor: "secondary.main" }}>
            <LockOutlinedIcon />
          </Avatar>
          <Typography component="h1" variant="h5">
            Sign up
          </Typography>
          {/* Render the registration form */}
          <RegisterForm handleSubmit={handleSubmit} error={error} />
        </Box>
        {/* Render the copyright information */}
        <Copyright sx={{ mt: 5 }} />
      </Container>
    </ThemeProvider>
  );
}
