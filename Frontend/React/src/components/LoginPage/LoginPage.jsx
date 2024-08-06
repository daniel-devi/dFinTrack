import { createTheme, CssBaseline, Grid, Paper, ThemeProvider } from "@mui/material";
// Components
import Copyright from "../Copyright";
import LoginForm from "./LoginForm";

const defaultTheme = createTheme();

// Main Login Page component
export default function LoginPage() {

// Component to display the background image
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
      <Grid container component="main" sx={{ height: "100vh" }}>
        <CssBaseline />
        <BackgroundImage />
        <Grid item xs={12} sm={8} md={5} component={Paper} elevation={6} square>
          <LoginForm />
          <Copyright sx={{ mt: 5 }} />
        </Grid>
      </Grid>
    </ThemeProvider>
  );
}
