## Student Name: Triya Augustine
## Student ID: 218859157

"""
Stub file for the is allocation feasible exercise.

Implement the function `is_allocation_feasible` to  Determine whether a set of resource requests can be satisfied 
given limited capacities. Take int account any possible constraints. See the lab handout
for full requirements.
"""
    
from typing import Dict, List, Union

Number = Union[int, float]


def is_allocation_feasible(
    resources: Dict[str, Number],
    requests: List[Dict[str, Number]]
) -> bool:
    """
    Determine whether a set of resource requests can be satisfied given limited capacities.
    At least one resource must remain partially unallocated after assignment.
    """

    used: Dict[str, Number] = {}

    # Initialize usage
    for resource in resources:
        used[resource] = 0

    for request in requests:
        # Structural validation
        if not isinstance(request, dict):
            raise ValueError("Each request must be a dictionary")

        for resource, amount in request.items():
            # Unknown resource
            if resource not in resources:
                return False

            # Invalid amount
            if amount < 0:
                return False

            used[resource] += amount

            # Capacity exceeded
            if used[resource] > resources[resource]:
                return False

    # NEW REQUIREMENT:
    # At least one resource must remain unallocated
    for resource in resources:
        if used[resource] < resources[resource]:
            return True

    # All resources fully consumed
    return False