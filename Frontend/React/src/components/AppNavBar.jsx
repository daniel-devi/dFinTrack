import { useState, useEffect } from "react";
/// Material UI
import Box from "@mui/material/Box";
import Button from "@mui/material/Button";
import Badge from "@mui/material/Badge";
import Typography from "@mui/material/Typography";
import Fade from "@mui/material/Fade";
import MenuItem from "@mui/material/MenuItem";
import { Link } from "@mui/material";
import Menu from "@mui/material/Menu";
import { createTheme} from '@mui/material/styles';
///Other Pages
import api from "./api";

/// Material Icon
import ShoppingCartIcon from "@mui/icons-material/ShoppingCart";

function AppAppBar() {
  const [isAuthorized, setIsAuthorized] = useState(null);
  const [user, setUser] = useState("");
  const [anchorEl, setAnchorEl] = useState(false);
  const open = Boolean(anchorEl);

  const handleClick = (event) => {
    setAnchorEl(event.currentTarget);
  };
  const handleClose = () => {
    setAnchorEl(null);
  };

  const LogInClick = () => {
    window.location.href = "http://localhost:5173/login";
  };
  
  const LogoutClick = () => {
    window.location.href = "http://localhost:5173/logout";
  };

  function CheckUser() {
    useEffect(() => {
      auth().catch(() => setIsAuthorized(false));
    }, []);

    const auth = async () => {
      const token = localStorage.getItem("access");
      if (token) {
        setIsAuthorized(true);
      }
    };
  }
  CheckUser();

  useEffect(() => {
    api.get("auth/users/me/").then((response) => {
      console.log(response.data);
      setUser(response.data.username);
    });
  }, []);

  return (
    <div>
          <Box sx={{ flex: 1, display: "flex" }}>
            <Typography variant="h5" >dFinTrack</Typography>
            <Link></Link>
            </Box>
            {/* !! REMEMBER TO CHANGE */}
            {isAuthorized !== null ? (
              <div >
                <Button
                  id="fade-button"
                  aria-controls={open ? "fade-menu" : undefined}
                  aria-haspopup="true"
                  aria-expanded={open ? "true" : undefined}
                  onClick={handleClick}
                  sx={{ color: "white", margin: "auto 0" }}
                >
                {user}
                </Button>
                <Menu
                  id="fade-menu"
                  MenuListProps={{
                    "aria-labelledby": "fade-button",
                  }}
                  anchorEl={anchorEl}
                  open={open}
                  onClose={handleClose}
                  TransitionComponent={Fade}
                >
                  <MenuItem>Profile</MenuItem>
                  <MenuItem>My account</MenuItem>
                  <MenuItem onClick={LogoutClick}>Logout</MenuItem>
                </Menu>
              </div>
            ) : (
              <h4 style={{margin: "0 5px"}} onClick={LogInClick}>Login</h4>
            )}

            <Button href="/dashboard">Dashboard</Button>

    </div>
  );
}

export default AppAppBar;

const theme = createTheme();

theme.typography.h3 = {
  fontSize: '1.2rem',
  '@media (min-width:600px)': {
    fontSize: '1.5rem',
  },
  [theme.breakpoints.up('md')]: {
    fontSize: '2.4rem',
  },
};