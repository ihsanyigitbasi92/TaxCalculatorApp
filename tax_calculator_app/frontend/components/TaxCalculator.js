import React from 'react';
import { View, Text, TextInput, Button } from 'react-native';

export default function TaxCalculator() {
  return (
    <View>
      <Text>Tax Calculator</Text>
      <TextInput placeholder="Income" />
      <TextInput placeholder="Deductions" />
      <TextInput placeholder="State" />
      <TextInput placeholder="Filing Status" />
      <Button title="Calculate" onPress={() => {}} />
    </View>
  );
}