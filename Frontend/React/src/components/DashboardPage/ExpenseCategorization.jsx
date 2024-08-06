import { Paper, Typography, Box } from '@mui/material';

// Component for expense categorization overview
const ExpenseCategorization = () => (
  <Paper elevation={3} style={{ padding: '16px' }}>
    <Typography variant="h6">Expense Categorization</Typography>
    <Box>
      <Typography variant="body1">
        Top categories: Food ($400), Transport ($300), Entertainment ($200).
      </Typography>
      {/* Additional expense categorization details */}
    </Box>
  </Paper>
);

export default ExpenseCategorization;
