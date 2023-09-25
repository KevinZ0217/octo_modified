"""
Contains basic logic for randomly zero-ing out keys in the task specification.
"""

import tensorflow as tf


def drop_keys_independent(
    traj: Dict[str, Any], drop_keys_probs: Dict[str, float]
) -> Dict[str, Any]:
    """
    Independently drop keys in the tasks dictionary.

    :param traj: A dictionary containing trajectory data. should have a "tasks" key.
    :param drop_keys_probs: A dictionary specifying the dropout probability for each key in tasks.
    :return: A dictionary with keys dropped out according to the specified probabilities.
    """
    new_tasks = traj["tasks"].copy()
    for key in drop_keys_probs:
        if key not in tasks:
            raise KeyError(f"{key} is not present in tasks dictionary.")

        new_tasks[key] = tf.where(
            tf.random.uniform([tf.shape(tasks[key])[0]]) < drop_keys_probs[key],
            tf.zeros_like(tasks[key]),
            tasks[key],
        )
    traj["tasks"] = new_tasks

    return traj
