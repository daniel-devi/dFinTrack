import { AppBar, Toolbar, Typography } from "@mui/material";

// Header component for the application
const Header = () => {
  return (
    <AppBar
      position="static"
      sx={{ zIndex: (theme) => theme.zIndex.drawer + 1 }}
    >
      <Toolbar>
        <Typography variant="h6">dFinTrack Dashboard</Typography>
      </Toolbar>
    </AppBar>
  );
};

export default Header;
