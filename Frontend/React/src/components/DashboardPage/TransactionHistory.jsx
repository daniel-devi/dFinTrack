import React from 'react';
import { Paper, Typography, List, ListItem, ListItemText, ListItemIcon, Chip } from '@mui/material';
import { AttachMoney, ShoppingCart, Restaurant, Payment } from '@mui/icons-material';

// Sample transaction data with categories and status
const transactions = [
  { date: '2024-08-01', description: 'Groceries', amount: '$50', category: 'Food', status: 'Completed' },
  { date: '2024-08-02', description: 'Electricity Bill', amount: '$100', category: 'Utilities', status: 'Pending' },
  { date: '2024-08-03', description: 'Gym Membership', amount: '$40', category: 'Health', status: 'Completed' },
  // Add more transactions here
];

// Map categories to icons
const categoryIcons = {
  Food: <Restaurant />,
  Utilities: <Payment />,
  Health: <ShoppingCart />,
  Other: <AttachMoney />
};

const TransactionHistory = () => (
  <Paper elevation={3} sx={{ padding: '16px' }}>
    <Typography variant="h6">Transaction History</Typography>
    <List>
      {transactions.map((transaction, index) => (
        <ListItem key={index}>
          <ListItemIcon>
            {categoryIcons[transaction.category] || <AttachMoney />}
          </ListItemIcon>
          <ListItemText
            primary={`${transaction.description} - ${transaction.amount}`}
            secondary={`${transaction.date} - ${transaction.category}`}
          />
          <Chip label={transaction.status} color={transaction.status === 'Completed' ? 'success' : 'warning'} />
        </ListItem>
      ))}
    </List>
  </Paper>
);

export default TransactionHistory;
