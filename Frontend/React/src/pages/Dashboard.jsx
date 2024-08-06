import React, { useState } from "react";
import { CssBaseline, Box } from "@mui/material";
import Sidebar from "../components/DashboardPage/SideBar";
import Header from "../components/DashboardPage/Header";
import DashboardPage from "../components/DashboardPage/DashboardPage";

function Dashboard() {
  // State to track the selected menu item
  const [selectedMenu, setSelectedMenu] = useState("dashboard");

  const drawerWidth = 240

  // Function to render the content based on the selected menu item
  const renderContent = () => {
    switch (selectedMenu) {
      case "dashboard":
        return <DashboardPage />;
      case "budget":
        return <div>Budget Component</div>;
      case "goals":
        return <div>Goals Component</div>;
      case "reports":
        return <div>Reports Component</div>;
      default:
        return <DashboardPage />;
    }
  };

  return (
    <Box sx={{ display: "flex" }}>
      <CssBaseline />
      {/* Main content area */}
      <Box
        component="main"
        sx={{
          flexGrow: 1,
          bgcolor: "background.default",
          p: 3,
          marginLeft: `${drawerWidth}px`,
        }}
      >
        {/* Header for the application */}
        <Header />
        {/* Sidebar for navigation */}
        <Sidebar onMenuClick={setSelectedMenu} />
        {/* Render the selected content */}
        {renderContent()}
      </Box>
    </Box>
  );
}

export default Dashboard;
