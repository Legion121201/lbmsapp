// store.js
import { configureStore } from '@reduxjs/toolkit';
import userReducer from './userSlice'; // Create this file later

export const store = configureStore({
  reducer: {
    user: userReducer,
    // ... other reducers if you have more slices
  },
});
