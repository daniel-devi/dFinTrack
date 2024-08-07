// src/styles/createTheme.js

import { createTheme as createMuiTheme } from '@mui/material/styles';

// You can customize your theme here
const createTheme = (options = {}) => {
  return createMuiTheme({
    ...options,
    // Add custom theme properties here
  });
};

export default createTheme;
