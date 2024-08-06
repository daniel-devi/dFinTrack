import React, { useState } from 'react';
import { Paper, Typography, IconButton, Tooltip } from '@mui/material';
import { Visibility, VisibilityOff } from '@mui/icons-material';

const CreditCardInfo = () => {
  const [showInfo, setShowInfo] = useState(false);

  // Toggle the visibility of confidential information
  const toggleShowInfo = () => {
    setShowInfo(!showInfo);
  };

  return (
    <Paper elevation={3} sx={{ padding: '16px' }}>
      <Typography variant="h6">Credit Card Information</Typography>
      <Typography variant="body1">
        Card Number: {showInfo ? '1234 5678 9876 5432' : '**** **** **** ****'}
      </Typography>
      <Typography variant="body1">
        Expiry Date: {showInfo ? '12/25' : '**/**'}
      </Typography>
      <Typography variant="body1">
        CVV: {showInfo ? '123' : '***'}
      </Typography>
      <Tooltip title={showInfo ? 'Hide Information' : 'Show Information'}>
        <IconButton onClick={toggleShowInfo}>
          {showInfo ? <VisibilityOff /> : <Visibility />}
        </IconButton>
      </Tooltip>
    </Paper>
  );
};

export default CreditCardInfo;
