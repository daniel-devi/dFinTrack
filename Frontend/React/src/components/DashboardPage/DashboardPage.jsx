import { Grid } from "@mui/material";
import BudgetOverview from "./BudgetOverview";
import ExpenseCategorization from "./ExpenseCategorization";
import FinancialGoals from "./FinancialGoals";
import ReportsAnalytics from "./ReportsAnalytics";
import TransactionHistory from "./TransactionHistory";
import CreditCardInfo from "./CreditCardInfo";

// Main Dashboard component
const DashboardPage = () => {
  return (
    <Grid container spacing={3} mt={"10px"}>
      <Grid item xs={6}>
        <BudgetOverview />
      </Grid>
      <Grid item xs={6}>
        <ExpenseCategorization />
      </Grid>
      <Grid item xs={6}>
        <FinancialGoals />
      </Grid>
      <Grid item xs={6}>
        <ReportsAnalytics />
      </Grid>
      <Grid item xs={12} md={6}>
        <TransactionHistory />
      </Grid>
      <Grid item xs={12} md={6}>
        <CreditCardInfo />
      </Grid>
    </Grid>
  );
};

export default DashboardPage;
