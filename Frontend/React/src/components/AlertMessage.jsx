import { useState } from "react";
import Alert from "@mui/material/Alert";
import IconButton from "@mui/material/IconButton";
import Collapse from "@mui/material/Collapse";
import CloseIcon from "@mui/icons-material/Close";

// Component for displaying an alert message with a close button
const AlertMessage = ({ open, setOpen, message }) => {
  return (
    <Collapse in={open}>
      <Alert
        action={
          <IconButton
            aria-label="close"
            color="inherit"
            size="small"
            onClick={() => setOpen(false)} // Close the alert when button is clicked
          >
            <CloseIcon fontSize="inherit" />
          </IconButton>
        }
        sx={{ mb: 2 }}
      >
        {message} {/* Display the message passed as a prop */}
      </Alert>
    </Collapse>
  );
};

export default AlertMessage;
