# class Phone:
#     def __init__(self, phone_number):
#         self.phone_number = phone_number
#         self.call_history = []   # list to keep call logs
#         self.messages = []       # list to keep messages (as dictionaries)

#     def call(self, other_phone):
#         """Simulate a call between two phones"""
#         log = f"{self.phone_number} called {other_phone.phone_number}"
#         print(log)
#         self.call_history.append(log)

#     def show_call_history(self):
#         """Display all calls made"""
#         if not self.call_history:
#             print("No calls yet.")
#         else:
#             print(" Call History:")
#             for call in self.call_history:
#                 print("-", call)

#     def send_message(self, other_phone, content):
#         """Send a message to another phone"""
#         message = {
#             "to": other_phone.phone_number,
#             "from": self.phone_number,
#             "content": content
#         }
#         self.messages.append(message)
#         print(f"Message sent from {self.phone_number} to {other_phone.phone_number}: {content}")

#     def show_outgoing_messages(self):
#         """Show messages I sent"""
#         print(f" Outgoing messages from {self.phone_number}:")
#         for msg in self.messages:
#             if msg["from"] == self.phone_number:
#                 print(f"To {msg['to']}: {msg['content']}")

#     def show_incoming_messages(self):
#         """Show messages I received"""
#         print(f" Incoming messages for {self.phone_number}:")
#         for msg in self.messages:
#             if msg["to"] == self.phone_number:
#                 print(f"From {msg['from']}: {msg['content']}")

#     def show_messages_from(self, number):
#         """Show messages received from a specific number"""
#         print(f" Messages from {number} to {self.phone_number}:")
#         for msg in self.messages:
#             if msg["from"] == number and msg["to"] == self.phone_number:
#                 print(msg["content"])
