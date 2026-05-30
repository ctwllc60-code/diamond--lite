import React, { useState } from 'react';

import {
  View,
  Text,
  TextInput,
  TouchableOpacity,
  StyleSheet,
  ScrollView,
} from 'react-native';


export default function HomeScreen() {

  const [message, setMessage] = useState('');

  const [chatHistory, setChatHistory] = useState([
    {
      sender: 'Diamond Lite',
      text: 'Welcome to Diamond Lite.',
    },
  ]);


  async function sendMessage() {

    if (!message.trim()) {
      return;
    }

    const userMessage = message;

    setChatHistory((previous) => [

      ...previous,

      {
        sender: 'You',
        text: userMessage,
      },
    ]);

    setMessage('');

    try {

      const response = await fetch(
        'http://10.10.0.237:5000/message',
        {
          method: 'POST',

          headers: {
            'Content-Type': 'application/json',
            'X-API-KEY': 'diamond_secure_dev_key',
          },

          body: JSON.stringify({

            user_id: 'mobile_user',

            session_id: 'mobile_session',

            device: 'android_mobile',

            message: userMessage,
          }),
        }
      );

      const data = await response.json();

      setChatHistory((previous) => [

        ...previous,

        {
          sender: 'Diamond Lite',
          text: data.response,
        },
      ]);

    } catch (error) {

      setChatHistory((previous) => [

        ...previous,

        {
          sender: 'Diamond Lite',
          text: 'Connection to backend failed.',
        },
      ]);
    }
  }


  return (

    <View style={styles.container}>

      <Text style={styles.header}>
        Diamond Lite
      </Text>

      <ScrollView style={styles.chatContainer}>

        {chatHistory.map((item, index) => (

          <View
            key={index}
            style={styles.messageBubble}
          >

            <Text style={styles.sender}>
              {item.sender}
            </Text>

            <Text style={styles.messageText}>
              {item.text}
            </Text>

          </View>
        ))}

      </ScrollView>

      <View style={styles.inputContainer}>

        <TextInput
          style={styles.input}
          placeholder="Type your message..."
          placeholderTextColor="#777"
          value={message}
          onChangeText={setMessage}
        />

        <TouchableOpacity
          style={styles.sendButton}
          onPress={sendMessage}
        >

          <Text style={styles.sendButtonText}>
            Send
          </Text>

        </TouchableOpacity>

      </View>

    </View>
  );
}


const styles = StyleSheet.create({

  container: {
    flex: 1,
    backgroundColor: '#000',
    paddingTop: 60,
    paddingHorizontal: 20,
  },

  header: {
    color: '#00ff99',
    fontSize: 30,
    fontWeight: 'bold',
    textAlign: 'center',
    marginBottom: 20,
  },

  chatContainer: {
    flex: 1,
  },

  messageBubble: {
    backgroundColor: '#1a1a1a',
    borderRadius: 12,
    padding: 15,
    marginBottom: 12,
  },

  sender: {
    color: '#00ff99',
    fontWeight: 'bold',
    marginBottom: 5,
  },

  messageText: {
    color: '#ffffff',
    fontSize: 16,
  },

  inputContainer: {
    flexDirection: 'row',
    alignItems: 'center',
    marginBottom: 20,
  },

  input: {
    flex: 1,
    backgroundColor: '#1a1a1a',
    color: '#ffffff',
    borderRadius: 10,
    paddingHorizontal: 15,
    paddingVertical: 12,
    marginRight: 10,
  },

  sendButton: {
    backgroundColor: '#00ff99',
    borderRadius: 10,
    paddingHorizontal: 20,
    paddingVertical: 12,
  },

  sendButtonText: {
    color: '#000',
    fontWeight: 'bold',
  },
});
