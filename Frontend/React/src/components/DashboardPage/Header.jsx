import React, { useState } from 'react';
import AppBar from "@mui/material/AppBar";
import Toolbar from "@mui/material/Toolbar";
import Button from "@mui/material/Button";
import Typography from "@mui/material/Typography";
import Modal from "@mui/material/Modal";
import Box from "@mui/material/Box";
import { 
  Category as CategoryIcon, 
  AddCircle as AddCircleIcon, 
  Receipt as ReceiptIcon, 
  AttachMoney as AttachMoneyIcon, 
  Analytics as AnalyticsIcon, 
  Report as ReportIcon 
} from "@mui/icons-material";

// Import modal forms
import CreateTransactionForm from './Forms/CreateTransactions';
//import CreateExpenseCategoryForm from './CreateExpenseCategoryForm';
//import CreateBudgetForm from './CreateBudgetForm';
//import CreateFinancialGoalForm from './CreateFinancialGoalForm';
//import CreateFinancialAnalyticsForm from './CreateFinancialAnalyticsForm';
///import CreateFinancialReportForm from './CreateFinancialReportForm';

// Modal style
const modalStyle = {
  position: 'absolute',
  top: '50%',
  left: '50%',
  transform: 'translate(-50%, -50%)',
  width: 650,
  bgcolor: 'background.paper',
  boxShadow: 25,
  p: 4,
};

// Header component
const Header = () => {
  // State for modal visibility
  const [open, setOpen] = useState(false);
  const [modalContent, setModalContent] = useState(null);

  // Open modal with specific content
  const handleOpen = (content) => {
    setModalContent(content);
    setOpen(true);
  };

  // Close modal
  const handleClose = () => setOpen(false);

  return (
    <>
      <AppBar position="static" sx={{ backgroundColor: '#fff', color: '#000' }}>
        <Toolbar sx={{ display: 'flex', justifyContent: 'space-between', flexWrap: 'wrap' }}>
          <Button
            startIcon={<CategoryIcon />}
            color="inherit"
            onClick={() => handleOpen(<CreateExpenseCategoryForm />)}
            sx={{ mx: 1 }}
          >
            Expense Category
          </Button>
          <Button
            startIcon={<AddCircleIcon />}
            color="inherit"
            onClick={() => handleOpen(<CreateTransactionForm onClose={() => handleClose} />)}
            sx={{ mx: 1 }}
          >
            Transaction
          </Button>
          <Button
            startIcon={<ReceiptIcon />}
            color="inherit"
            onClick={() => handleOpen(<CreateBudgetForm />)}
            sx={{ mx: 1 }}
          >
            Budget
          </Button>
          <Button
            startIcon={<AttachMoneyIcon />}
            color="inherit"
            onClick={() => handleOpen(<CreateFinancialGoalForm />)}
            sx={{ mx: 1 }}
          >
            Financial Goal
          </Button>
          <Button
            startIcon={<AnalyticsIcon />}
            color="inherit"
            onClick={() => handleOpen(<CreateFinancialAnalyticsForm />)}
            sx={{ mx: 1 }}
          >
            Financial Analytics
          </Button>
          <Button
            startIcon={<ReportIcon />}
            color="inherit"
            onClick={() => handleOpen(<CreateFinancialReportForm />)}
            sx={{ mx: 1 }}
          >
            Financial Report
          </Button>
        </Toolbar>
      </AppBar>

      {/* Modal component */}
      <Modal open={open} onClose={handleClose}>
        <Box sx={modalStyle}>
          {modalContent}
        </Box>
      </Modal>
    </>
  );
};

export default Header;