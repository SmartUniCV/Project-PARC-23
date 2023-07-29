import rospy

import .utils.vision as v
import .utils.ruler as r

from .perceiver import AgribotPerceiver
from .utils import SteppedAction, Action
from .utils import ForgetfulMemory, BasicQueue


class AgribotPlanner:
    def __init__(self, perception: AgribotPerceiver) -> None:
        self._percept = perception
        self._last_actions_memory = ForgetfulMemory()
        self._next_actions_queue = BasicQueue()

    @property
    def _has_enqueued_actions(self) -> bool:
        return not self._next_actions_queue.empty()

    def _resolve_enqueued_action(self) -> Action:
        """Returns the next action in the queue, removing it from the structure."""
        if self._has_enqueued_actions:
            return self._next_actions_queue.dequeue()
        return None

    def enqueue_action(self, action: Action) -> None:
        """Add a new action to the action queue."""
        self._next_actions_queue.enqueue(action)

    def _process_env_perception(self) -> dict:
        return {} # TODO

    def plan_action(self) -> Action:
        """Analyse the information from the environment and determine the
        best course of action to be taken by the robot."""
        if self._has_enqueued_actions:
            return self._resolve_enqueued_action()

        kwargs = self._process_env_perception()

        if (finish := self._finish_navigation(**kwargs)) is not None:
            return finish
        elif (turn := self._make_a_turn(**kwargs)) is not None:
            return turn
        return self._move_forward(**kwargs)

    def _make_a_turn(self) -> Action:
        return None # TODO

    def _move_forward(self) -> Action:
        return None # TODO

    def _finish_navigation(self) -> Action:
        return None # TODO