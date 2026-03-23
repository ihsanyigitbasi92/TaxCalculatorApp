import React from 'react';
import { View, Text, TextInput, Button } from 'react-native';

export default function Register() {
  return (
    <View>
      <Text>Register</Text>
      <TextInput placeholder="Email" />
      <TextInput placeholder="Password" secureTextEntry={true} />
      <Button title="Register" onPress={() => {}} />
    </View>
  );
}