import {
  Drawer,
  List,
  ListItem,
  ListItemIcon,
  ListItemText,
} from "@mui/material";
import { Dashboard, Category, TrendingUp, BarChart } from "@mui/icons-material";

// Sidebar component for navigation

const drawerWidth = 240;

const Sidebar = ({ onMenuClick }) => {
  return (
    <Drawer
      variant="permanent"
      sx={{
        width: drawerWidth,
        flexShrink: 0,
        [`& .MuiDrawer-paper`]: { width: drawerWidth, boxSizing: "border-box" },
      }}
    >
      <List>
        {/* Dashboard menu item */}
        <ListItem button onClick={() => onMenuClick("dashboard")}>
          <ListItemIcon>
            <Dashboard />
          </ListItemIcon>
          <ListItemText primary="Dashboard" />
        </ListItem>
        {/* Budget menu item */}
        <ListItem button onClick={() => onMenuClick("budget")}>
          <ListItemIcon>
            <Category />
          </ListItemIcon>
          <ListItemText primary="Budget" />
        </ListItem>
        {/* Goals menu item */}
        <ListItem button onClick={() => onMenuClick("goals")}>
          <ListItemIcon>
            <TrendingUp />
          </ListItemIcon>
          <ListItemText primary="Goals" />
        </ListItem>
        {/* Reports menu item */}
        <ListItem button onClick={() => onMenuClick("reports")}>
          <ListItemIcon>
            <BarChart />
          </ListItemIcon>
          <ListItemText primary="Reports" />
        </ListItem>
      </List>
    </Drawer>
  );
};

export default Sidebar;
