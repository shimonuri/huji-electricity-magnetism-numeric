import logging
import pickle
import copy

import space
import boundary_setter

logging.basicConfig(level=logging.INFO)


class RelaxationModel:
    def __init__(self, rmax, zmax, h, max_diff):
        self._previous_space = None
        self.space = space.Space(rmax, zmax, h)
        self._max_diff = max_diff
        self._is_initialized = False

    def initDatabase(self):
        boundary_setter.set_boundary(self.space)
        self._is_initialized = True

    def relax(self, pickle_path):
        if not self._is_initialized:
            logging.error("Not initialized")
            return

        logging.info("Relaxation Model Begins")
        iteration_number = 0
        while not self._is_finished(self._max_diff):
            logging.info(f"Iteration {iteration_number} Begins")
            logging.info(f"(i.{iteration_number}) Saving Space Copy")
            self._save_copy()
            logging.info(f"(i.{iteration_number}) Updating Space")
            self._update_space(self.space.h)
            logging.info(f"Iteration {iteration_number} Finished")

        logging.info(f"Relaxation Model is Finished")
        logging.info(f"Dumping space into pickle ({pickle_path})")
        self._dump_space(pickle_path)

    def _dump_space(self, pickle_path):
        with open(pickle_path, "wb") as fd:
            pickle.dump(self.space, fd)

    def _save_copy(self):
        del self._previous_space
        self._previous_space = copy.deepcopy(self.space)

    def _is_finished(self, max_diff):
        actual_max_diff = max(
            (
                self.space.get_point(r, z) / self._previous_space.get_value(r, z)
                for r, z in self.space.get_changeable()
            )
        )
        logging.info(f"Current diff is {actual_max_diff}")
        if actual_max_diff <= max_diff:
            return False

        return True

    def _update_space(self, h):
        for r, z in self.space.get_changeable():
            self.space.set_point(
                r, z, self._get_new_potential(h, r, z), is_changeable=True
            )

    def _get_new_potential(self, h, r, z):
        r_plus = self.space.get_point(r + h, z)
        r_minus = self.space.get_point(r - h, z)
        z_plus = self.space.get_point(r, z + h)
        z_minus = self.space.get_point(r, z - h)
        r_delta = h / (2 * r)
        new_potential = r_plus * (1 + r_delta)
        new_potential += r_minus * (1 - r_delta)
        new_potential += z_plus + z_minus
        new_potential *= 1 / 4
        return new_potential
