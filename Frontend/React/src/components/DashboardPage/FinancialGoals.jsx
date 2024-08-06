import { Paper, Typography, Box } from '@mui/material';

// Component for financial goals overview
const FinancialGoals = () => (
  <Paper elevation={3} style={{ padding: '16px' }}>
    <Typography variant="h6">Financial Goals</Typography>
    <Box>
      <Typography variant="body1">
        Savings goal: $5000 by the end of the year. Progress: 60%
      </Typography>
      {/* Additional financial goals details */}
    </Box>
  </Paper>
);

export default FinancialGoals;
