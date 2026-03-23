import React from 'react';
import { View, Text, TextInput, Button } from 'react-native';

export default function Login() {
  return (
    <View>
      <Text>Login</Text>
      <TextInput placeholder="Email" />
      <TextInput placeholder="Password" secureTextEntry={true} />
      <Button title="Login" onPress={() => {}} />
    </View>
  );
}