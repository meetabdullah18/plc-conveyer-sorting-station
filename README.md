# plc-conveyer-sorting-station
# Smart Conveyor Sorting Station (Siemens TIA Portal V21)

A simulated conveyor sorting station built in **Siemens TIA Portal V21**. Two sensors detect an incoming object and its type, ladder logic decides which of two gates to fire, and two independent counters track throughput by type. A hardwired **E-Stop** interlock overrides every output regardless of system state.

---

## Architecture

<img width="2720" height="2144" alt="conveyor_sorting_architecture" src="https://github.com/user-attachments/assets/2fe60cbb-2d38-474a-8e1c-6c9992951c30" />


---

## How it works

Every scan cycle, the PLC reads **ObjectSensor** and **TypeSensor** as fresh input values.

The decision rungs combine those two inputs to set either **SortA_Request** or **SortB_Request**—never both, since the type sensor's state is mutually exclusive by design.

Whichever request is active fires the matching gate, and each gate activation increments its own counter. This allows throughput for each object type to be tracked independently rather than as one combined total.

**SystemEnabled**, driven by the **E-Stop**, is placed as an additional series contact on every output rung. As soon as the E-Stop is activated, every output drops on the next PLC scan regardless of what the sorting logic was requesting.

---

## Screenshots

### Ladder Logic
<!-- Replace with your screenshot -->

<img width="452" height="254" alt="image" src="https://github.com/user-attachments/assets/c0021e00-71f5-42af-a183-8188a04e5312" />

### Counters & Sorting Logic

<img width="452" height="253" alt="image" src="https://github.com/user-attachments/assets/c3c3070b-da81-4605-bea7-1aacd20c01f8" />

### Safety and System Control Logic

<img width="554" height="209" alt="image" src="https://github.com/user-attachments/assets/818d0c4b-b7b1-48d8-af45-c9a7d43d8c95" />
<img width="759" height="329" alt="image" src="https://github.com/user-attachments/assets/0d167b14-0c75-4c52-92af-185a8eeb7e5a" />
<img width="452" height="194" alt="image" src="https://github.com/user-attachments/assets/1a7abd07-daa8-4fd7-9ceb-fe770378e895" />
<img width="452" height="161" alt="image" src="https://github.com/user-attachments/assets/b58bf303-1029-4cbd-afe9-d761b5e1ffb5" />

### HMI During Operation
<!-- Replace with your screenshot -->

<img width="447" height="251" alt="image" src="https://github.com/user-attachments/assets/4bc7014c-284c-44f8-aaa4-c036731a7c39" />
<img width="452" height="384" alt="image" src="https://github.com/user-attachments/assets/377a5f37-91b2-42fb-a252-f2621b2873b5" />
<img width="452" height="350" alt="image" src="https://github.com/user-attachments/assets/a1e4f72f-696c-4d42-b98d-9ed220608b92" />


---

## What I Learned

- The PLC scan cycle makes ladder logic behave like a continuously refreshed control system rather than a one-time script.
- Implementing the E-Stop after the sorting logic highlighted an important industrial design principle: safety should sit above the control logic so it cannot be bypassed by any process state.
- This project introduced me to state-based decision making, where outputs depend on combinations of multiple inputs rather than individual signals.
- I also learned the practical difference between timers and counters:
  - **Timers** measure how long a condition remains true (used for gate hold-open time).
  - **Counters** measure how many times an event occurs (used for tracking sorted objects).
