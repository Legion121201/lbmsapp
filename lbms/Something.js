// SomeComponent.js
import React from 'react';
import { useSelector } from 'react-redux';

const SomeComponent = () => {
  const user = useSelector((state) => state.user);

  // ... Use user state as needed
};
