import { Paper, Typography, Box } from '@mui/material';

// Component for budget tracking overview
const BudgetOverview = () => (
  <Paper elevation={3} style={{ padding: '16px' }}>
    <Typography variant="h6">Budget Tracking</Typography>
    <Box>
      <Typography variant="body1">
        You have spent $1200 out of your $2000 budget for this month.
      </Typography>
      {/* Additional budget tracking details */}
    </Box>
  </Paper>
);

export default BudgetOverview;
