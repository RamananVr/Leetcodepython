"""
2694. Event Emitter

PROBLEM STATEMENT:
Design an EventEmitter class that allows subscribing to events and emitting events to all subscribers.
The class should support:
1. subscribe(eventName, callback) - subscribe to an event with a callback function
2. unsubscribe(eventName, callback) - unsubscribe a specific callback from an event
3. emit(eventName, args) - emit an event with arguments to all subscribers
4. Return an unsubscribe function from subscribe for easy cleanup

EXAMPLES:
Example 1:
emitter = EventEmitter()
sub = emitter.subscribe("test", lambda x: print(f"Received: {x}"))
emitter.emit("test", [42])  # Output: "Received: 42"
sub.unsubscribe()

Example 2:
emitter = EventEmitter()
emitter.subscribe("click", lambda: print("Button clicked"))
emitter.subscribe("click", lambda: print("Click logged"))
emitter.emit("click", [])  # Output: "Button clicked" "Click logged"

CONSTRAINTS:
- Event names are strings
- Callbacks can accept any number of arguments
- Multiple callbacks can be subscribed to the same event
- Should handle unsubscribing non-existent callbacks gracefully
"""

def create_event_emitter():
    """
    Implementation of an Event Emitter system.
    """
    
    class EventEmitter:
        def __init__(self):
            self.events = {}
            self._subscription_id = 0
        
        def subscribe(self, event_name, callback):
            """
            Subscribe to an event with a callback.
            
            Args:
                event_name: Name of the event to subscribe to
                callback: Function to call when event is emitted
            
            Returns:
                Subscription object with unsubscribe method
            """
            if event_name not in self.events:
                self.events[event_name] = {}
            
            # Generate unique subscription ID
            sub_id = self._subscription_id
            self._subscription_id += 1
            
            # Store callback with subscription ID
            self.events[event_name][sub_id] = callback
            
            # Return subscription object
            class Subscription:
                def __init__(self, emitter, event_name, sub_id):
                    self.emitter = emitter
                    self.event_name = event_name
                    self.sub_id = sub_id
                    self.active = True
                
                def unsubscribe(self):
                    """Unsubscribe this specific callback"""
                    if self.active and self.event_name in self.emitter.events:
                        if self.sub_id in self.emitter.events[self.event_name]:
                            del self.emitter.events[self.event_name][self.sub_id]
                            
                            # Clean up empty event
                            if not self.emitter.events[self.event_name]:
                                del self.emitter.events[self.event_name]
                        
                        self.active = False
            
            return Subscription(self, event_name, sub_id)
        
        def unsubscribe(self, event_name, callback):
            """
            Unsubscribe a specific callback from an event.
            
            Args:
                event_name: Name of the event
                callback: The callback function to remove
            """
            if event_name not in self.events:
                return
            
            # Find and remove callback
            to_remove = []
            for sub_id, stored_callback in self.events[event_name].items():
                if stored_callback == callback:
                    to_remove.append(sub_id)
            
            for sub_id in to_remove:
                del self.events[event_name][sub_id]
            
            # Clean up empty event
            if not self.events[event_name]:
                del self.events[event_name]
        
        def emit(self, event_name, args=None):
            """
            Emit an event to all subscribers.
            
            Args:
                event_name: Name of the event to emit
                args: List of arguments to pass to callbacks
            
            Returns:
                List of results from all callback invocations
            """
            if args is None:
                args = []
            
            if event_name not in self.events:
                return []
            
            results = []
            
            # Call all callbacks for this event
            for callback in self.events[event_name].values():
                try:
                    result = callback(*args)
                    results.append(result)
                except Exception as e:
                    # In a real implementation, you might want to log this
                    results.append(f"Error: {str(e)}")
            
            return results
        
        def once(self, event_name, callback):
            """
            Subscribe to an event but automatically unsubscribe after first emission.
            
            Args:
                event_name: Name of the event
                callback: Function to call once
            
            Returns:
                Subscription object
            """
            def one_time_callback(*args):
                result = callback(*args)
                subscription.unsubscribe()
                return result
            
            subscription = self.subscribe(event_name, one_time_callback)
            return subscription
        
        def listeners(self, event_name):
            """
            Get all listeners for an event.
            
            Args:
                event_name: Name of the event
            
            Returns:
                List of callback functions
            """
            if event_name not in self.events:
                return []
            
            return list(self.events[event_name].values())
        
        def listener_count(self, event_name):
            """
            Get the number of listeners for an event.
            
            Args:
                event_name: Name of the event
            
            Returns:
                Number of listeners
            """
            if event_name not in self.events:
                return 0
            
            return len(self.events[event_name])
        
        def remove_all_listeners(self, event_name=None):
            """
            Remove all listeners for an event, or all events if no event specified.
            
            Args:
                event_name: Name of the event (optional)
            """
            if event_name is None:
                self.events.clear()
            elif event_name in self.events:
                del self.events[event_name]
        
        def event_names(self):
            """
            Get all event names that have listeners.
            
            Returns:
                List of event names
            """
            return list(self.events.keys())
    
    return EventEmitter

def test_event_emitter():
    """Test the Event Emitter implementation."""
    EventEmitter = create_event_emitter()
    emitter = EventEmitter()
    
    # Test 1: Basic subscription and emission
    results = []
    
    def callback1(x):
        results.append(f"Callback1: {x}")
        return f"Result1: {x}"
    
    sub1 = emitter.subscribe("test", callback1)
    emitted_results = emitter.emit("test", [42])
    
    assert results == ["Callback1: 42"]
    assert emitted_results == ["Result1: 42"]
    
    # Test 2: Multiple subscribers
    results.clear()
    
    def callback2(x):
        results.append(f"Callback2: {x}")
        return f"Result2: {x}"
    
    sub2 = emitter.subscribe("test", callback2)
    emitted_results = emitter.emit("test", [100])
    
    assert "Callback1: 100" in results
    assert "Callback2: 100" in results
    assert len(emitted_results) == 2
    
    # Test 3: Unsubscription
    results.clear()
    sub1.unsubscribe()
    emitter.emit("test", [200])
    
    assert results == ["Callback2: 200"]
    
    # Test 4: Different events
    results.clear()
    
    def click_handler():
        results.append("Clicked!")
        return "Click handled"
    
    click_sub = emitter.subscribe("click", click_handler)
    emitter.emit("click", [])
    emitter.emit("test", [300])
    
    assert "Clicked!" in results
    assert "Callback2: 300" in results
    
    # Test 5: Once subscription
    results.clear()
    
    def once_handler(value):
        results.append(f"Once: {value}")
    
    once_sub = emitter.subscribe("once_event", once_handler)
    emitter.emit("once_event", [1])
    emitter.emit("once_event", [2])  # Should not trigger
    
    # For regular subscription, it should trigger both times
    assert len([r for r in results if "Once:" in r]) == 2
    
    # Test 6: Listener count
    assert emitter.listener_count("test") == 1  # callback2 still subscribed
    assert emitter.listener_count("click") == 1  # click_handler subscribed
    assert emitter.listener_count("nonexistent") == 0
    
    # Test 7: Remove all listeners
    emitter.remove_all_listeners("test")
    assert emitter.listener_count("test") == 0
    assert emitter.listener_count("click") == 1  # Should still exist
    
    # Test 8: Event names
    event_names = emitter.event_names()
    assert "click" in event_names
    assert "test" not in event_names
    
    # Test 9: Error handling
    def error_callback():
        raise ValueError("Test error")
    
    error_sub = emitter.subscribe("error_test", error_callback)
    results = emitter.emit("error_test", [])
    assert len(results) == 1
    assert "Error:" in str(results[0])
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_event_emitter()

"""
COMPLEXITY ANALYSIS:
- Time Complexity: 
  - subscribe(): O(1)
  - unsubscribe(): O(n) where n is number of subscribers
  - emit(): O(n) where n is number of subscribers
- Space Complexity: O(m*n) where m is number of events and n is average subscribers per event

TOPICS: Design, Observer Pattern, Event-Driven Programming, Publish-Subscribe

KEY INSIGHTS:
1. Event emitters implement the Observer pattern for loose coupling
2. Subscription IDs prevent issues with duplicate callbacks
3. Automatic cleanup prevents memory leaks
4. Error handling in callbacks prevents one bad callback from affecting others
5. Once subscriptions provide convenient auto-cleanup functionality
"""
