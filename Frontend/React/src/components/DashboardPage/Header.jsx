import React from 'react';
import AppBar from "@mui/material/AppBar";
import Toolbar from "@mui/material/Toolbar";
import Button from "@mui/material/Button";
import Typography from "@mui/material/Typography";
import { 
  Category as CategoryIcon, 
  AddCircle as AddCircleIcon, 
  Receipt as ReceiptIcon, 
  AttachMoney as AttachMoneyIcon, 
  Analytics as AnalyticsIcon, 
  Report as ReportIcon 
} from "@mui/icons-material";
/// Pages
import CreateTransaction from './CreateTransactions';

const Header = () => {
  // Handlers for button actions
  const handleCreateExpenseCategory = () => {
    // Implement the logic to create Expense Category
  };

  const handleCreateTransaction = () => {
    // Implement the logic to create Transaction
    <CreateTransaction/>
  };

  const handleCreateBudget = () => {
    // Implement the logic to create Budget
  };

  const handleCreateFinancialGoal = () => {
    // Implement the logic to create Financial Goal
  };

  const handleCreateFinancialAnalytics = () => {
    // Implement the logic to create Financial Analytics
  };

  const handleCreateFinancialReport = () => {
    // Implement the logic to create Financial Report
  };

  return (
    <AppBar position="static" sx={{ backgroundColor: '#fff', color: '#000' }}>
      <Toolbar sx={{ display: 'flex', justifyContent: 'space-between', flexWrap: 'wrap' }}>
        <Button
          startIcon={<CategoryIcon />}
          color="inherit"
          onClick={handleCreateExpenseCategory}
          sx={{ mx: 1 }}
        >
          Expense Category
        </Button>
        <Button
          startIcon={<AddCircleIcon />}
          color="inherit"
          onClick={handleCreateTransaction}
          sx={{ mx: 1 }}
        >
          Transaction
        </Button>
        <Button
          startIcon={<ReceiptIcon />}
          color="inherit"
          onClick={handleCreateBudget}
          sx={{ mx: 1 }}
        >
          Budget
        </Button>
        <Button
          startIcon={<AttachMoneyIcon />}
          color="inherit"
          onClick={handleCreateFinancialGoal}
          sx={{ mx: 1 }}
        >
          Financial Goal
        </Button>
        <Button
          startIcon={<AnalyticsIcon />}
          color="inherit"
          onClick={handleCreateFinancialAnalytics}
          sx={{ mx: 1 }}
        >
          Financial Analytics
        </Button>
        <Button
          startIcon={<ReportIcon />}
          color="inherit"
          onClick={handleCreateFinancialReport}
          sx={{ mx: 1 }}
        >
          Financial Report
        </Button>
      </Toolbar>
    </AppBar>
  );
};

export default Header;
