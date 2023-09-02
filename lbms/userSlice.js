// userSlice.js
import { createSlice, createAsyncThunk } from '@reduxjs/toolkit';
import axios from 'axios';


import { createAsyncThunk, createSlice } from '@reduxjs/toolkit';
import axios from 'axios';

export const fetchUserData = createAsyncThunk('user/fetchUserData', async (userId) => {
  const response = await axios.get(`/api/users/${userId}/`); // Adjust the API endpoint
  return response.data;
});




export const registerUser = createAsyncThunk('user/register', async (userData) => {
  try {
    const response = await axios.post('/api/register/', userData);
    return response.data;
  } catch (error) {
    throw error.response.data;
  }
});

const userSlice = createSlice({
  name: 'user',
  initialState: {},
  reducers: {
    // Other reducers for user-related actions (e.g., login, logout)
  },
  extraReducers: (builder) => {
    builder.addCase(registerUser.fulfilled, (state, action) => {
      // Handle registration success, update state if needed
    });
    builder.addCase(registerUser.rejected, (state, action) => {
      // Handle registration error, update state if needed
    });
  },
});

export default userSlice.reducer;
