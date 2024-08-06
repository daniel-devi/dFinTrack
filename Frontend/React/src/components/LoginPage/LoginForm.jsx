import { useState, useEffect } from "react";
import {
  Avatar,
  Button,
  TextField,
  FormControlLabel,
  Checkbox,
  Grid,
  Box,
  Typography,
  Link,
} from "@mui/material";
import LockOutlinedIcon from "@mui/icons-material/LockOutlined";
import AlertMessage from "../AlertMessage";
import api from "../api";
import { ACCESS_TOKEN, REFRESH_TOKEN } from "../constants";

// Component to handle login form and submission
const LoginForm = () => {
  const [userList, setUserList] = useState([]);
  const [open, setOpen] = useState(false);
  const [error, setError] = useState(false);
  const [errorMessageUsername, setErrorMessageUsername] = useState("");
  const [errorMessagePassword, setErrorMessagePassword] = useState("");
  const [dUsername, setDUsername] = useState("");

  // Fetch the list of usernames when the component mounts
  useEffect(() => {
    api
      .get("Accounts-api/User/get-username")
      .then((response) => {
        setUserList(response.data);
      })
      .catch((error) => {
        // Do Nothing
      });
  }, []);

  // Function to find a username by email
  const findUsername = async (theEmail) => {
    try {
      let res = await api.get(`Accounts-api/User/get-user-through-email/${theEmail}`);
      setDUsername(res.data[0].username);
    } catch (error) {
      // Do Nothing
    }
  };

  // Handle form submission for login
  const handleSubmit = async (event) => {
    event.preventDefault();
    const data = new FormData(event.currentTarget);
    let email = data.get("email");
    await findUsername(email); // Wait for username to be found

    try {
      let res = await api.post("api/token/", {
        username: dUsername,
        password: data.get("password"),
      });
      if (res.status === 200) {
        // If login is successful, store tokens and user info
        localStorage.setItem(ACCESS_TOKEN, res.data.access);
        localStorage.setItem(REFRESH_TOKEN, res.data.refresh);
        localStorage.setItem("User", res.data.access);
        setErrorMessagePassword("");
        setErrorMessageUsername("");
        setOpen(true);
        // Redirect to home page after a short delay
        setTimeout(() => {
          window.location.href = "http://localhost:5173/";
        }, 3500);
      }
    } catch (error) {
      if (error.response.status !== 200) {
        // Check for bad request
        setError(true);
        let foundUser = Boolean(
          userList.find((user) => user.username === dUsername)
        );
        setErrorMessageUsername(foundUser ? "" : "User Not Found");
        setErrorMessagePassword("Password Incorrect");
      }
    }
  };

  return (
    <Box
      sx={{
        my: 8,
        mx: 4,
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
      }}
    >
      <AlertMessage
        open={open}
        setOpen={setOpen}
        message={"Login Successful"}
      />
      <Avatar sx={{ m: 1, bgcolor: "secondary.main" }}>
        <LockOutlinedIcon />
      </Avatar>
      <Typography component="h1" variant="h5">
        Login
      </Typography>
      <Box
        component="form"
        onSubmit={handleSubmit}
        sx={{ mt: 1 }}
        validate="true"
      >
        <TextField
          margin="normal"
          required
          fullWidth
          id="email"
          label="Email"
          name="email"
          autoComplete="email"
          error={error}
          helperText={errorMessageUsername}
          autoFocus
          placeholder="someone@example.com"
        />
        <TextField
          margin="normal"
          required
          fullWidth
          name="password"
          label="Password"
          type="password"
          id="password"
          autoComplete="current-password"
          error={error}
          helperText={errorMessagePassword}
        />
        <Grid container justifyContent={"space-between"}>
          <FormControlLabel
            control={<Checkbox value="remember" color="primary" />}
            label="Remember me"
          />
          <Link href="#" variant="body2" sx={{ padding: "7px 0" }}>
            Forgot password?
          </Link>
        </Grid>

        <Button
          type="submit"
          fullWidth
          variant="contained"
          sx={{ mt: 3, mb: 2 }}
        >
          Log In
        </Button>

        <Grid container spacing={1}>
          <Typography variant="body3">Don't have an Account</Typography>
          <Link href="register" variant="body3">
            {" Sign Up"}
          </Link>
          <Grid item></Grid>
        </Grid>
      </Box>
    </Box>
  );
};

export default LoginForm;
