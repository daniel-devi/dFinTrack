import { useState, useEffect } from "react";
import api from "../api";
import {
  Button,
  TextField,
  MenuItem,
  FormControl,
  InputLabel,
  Select,
  Box,
} from "@mui/material";

const CreateTransaction = () => {
  // State to manage form data
  const [transactionType, setTransactionType] = useState("");
  const [status, setStatus] = useState("");
  const [currency, setCurrency] = useState("");
  const [amount, setAmount] = useState("");
  const [category, setCategory] = useState("");
  const [description, setDescription] = useState("");

  // States to manage options and loading
  const [transactionTypes, setTransactionTypes] = useState([]);
  const [statuses, setStatuses] = useState([]);
  const [categories, setCategories] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  // Fetch options for select fields
  useEffect(() => {
    const fetchOptions = async () => {
      setLoading(true);
      setError(null);

      try {
        // Replace with your actual API endpoints
        const [transactionTypesResponse, statusesResponse, categoriesResponse] =
          await Promise.all([
            api.get("/api/transaction-types/"),
            api.get("/api/statuses/"),
            api.get("/api/categories/"),
          ]);

        setTransactionTypes(transactionTypesResponse.data);
        setStatuses(statusesResponse.data);
        setCategories(categoriesResponse.data);
      } catch (err) {
        setError("Failed to load options. Please try again.");
      } finally {
        setLoading(false);
      }
    };

    fetchOptions();
  }, []);

  const handleSubmit = async (event) => {
    event.preventDefault();

    setLoading(true);
    setError(null);

    // Prepare data to send
    const transactionData = {
      user,
      account,
      transaction_type: transactionType,
      status,
      currency,
      amount,
      category,
      description,
    };

    try {
      // POST request to create a new transaction
      await api.post("/api/transactions/", transactionData);
      alert("Transaction created successfully!");

      // Reset form
      setUser("");
      setAccount("");
      setTransactionType("");
      setStatus("");
      setCurrency("");
      setCategory("");
      setDescription("");
    } catch (err) {
      setError("Failed to create transaction. Please try again.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <form onSubmit={handleSubmit} style={{ width: "400px", margin: "auto" }}>
      <h2>Create Transaction</h2>

      <Box>
        <FormControl fullWidth margin="normal">
          <InputLabel>Currency</InputLabel>
          <Select
            value={currency}
            onChange={(e) => setCurrency(e.target.value)}
            disabled={loading}
          >
            <MenuItem value="USD">USD - United States Dollar</MenuItem>
            <MenuItem value="EUR">EUR - Euro</MenuItem>
            <MenuItem value="GBP">GBP - British Pound</MenuItem>
            {/* Add more currencies as needed */}
          </Select>
        </FormControl>

        <TextField
          fullWidth
          type="number"
          label="Amount"
          value={amount}
          onChange={(e) => setAmount(e.target.value)}
          margin="normal"
        />

        <TextField
          fullWidth
          label="Description"
          value={description}
          onChange={(e) => setDescription(e.target.value)}
          margin="normal"
          multiline
          rows={4}
        />
      </Box>

      <FormControl fullWidth margin="normal">
        <InputLabel>Transaction Type</InputLabel>
        <Select
          value={transactionType}
          onChange={(e) => setTransactionType(e.target.value)}
          disabled={loading}
        >
          {transactionTypes.map((type) => (
            <MenuItem key={type.id} value={type.id}>
              {type.name}
            </MenuItem>
          ))}
        </Select>
      </FormControl>

      <FormControl fullWidth margin="normal">
        <InputLabel>Status</InputLabel>
        <Select
          value={status}
          onChange={(e) => setStatus(e.target.value)}
          disabled={loading}
        >
          {statuses.map((statusOption) => (
            <MenuItem key={statusOption.id} value={statusOption.id}>
              {statusOption.name}
            </MenuItem>
          ))}
        </Select>
      </FormControl>

      <FormControl fullWidth margin="normal">
        <InputLabel>Category</InputLabel>
        <Select
          value={category}
          onChange={(e) => setCategory(e.target.value)}
          disabled={loading}
        >
          {categories.map((categoryOption) => (
            <MenuItem key={categoryOption.id} value={categoryOption.id}>
              {categoryOption.name}
            </MenuItem>
          ))}
        </Select>
      </FormControl>

      {error && <p style={{ color: "red" }}>{error}</p>}
      <Button
        type="submit"
        variant="contained"
        color="primary"
        disabled={loading}
      >
        {loading ? "Creating..." : "Create Transaction"}
      </Button>
    </form>
  );
};

export default CreateTransaction;
