import React from 'react';
import { View, Text, TextInput, Button } from 'react-native';

export default function Profile() {
  return (
    <View>
      <Text>Profile</Text>
      <TextInput placeholder="Name" />
      <TextInput placeholder="Email" />
      <Button title="Update" onPress={() => {}} />
    </View>
  );
}