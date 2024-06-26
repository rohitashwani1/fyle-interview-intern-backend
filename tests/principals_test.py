from core.models.assignments import AssignmentStateEnum, GradeEnum
from core import db
from core.models.assignments import Assignment, AssignmentStateEnum, GradeEnum

def test_get_assignments(client, h_principal):
    response = client.get(
        '/principal/assignments',
        headers=h_principal
    )

    assert response.status_code == 200

    data = response.json['data']
    for assignment in data:
        assert assignment['state'] in [AssignmentStateEnum.SUBMITTED, AssignmentStateEnum.GRADED]

def test_get_teachers(client, h_principal):
    response = client.get(
        '/principal/teachers',
        headers=h_principal
    )

    assert response.status_code == 200

def test_grade_assignment_draft_assignment(client, h_principal):
    """
    failure case: If an assignment is in Draft state, it cannot be graded by principal
    """
    assignment = Assignment(
            student_id=1,
            content='test content',
            state=AssignmentStateEnum.DRAFT
    )
    db.session.add(assignment)
    db.session.commit()
    response = client.post(
        '/principal/assignments/grade',
        json={
            'id': assignment.id,
            'grade': GradeEnum.A.value
        },
        headers=h_principal
    )
    # Here the assiggment mentioned was not in DRAFT state
    # So replace the id of assignment with a draft state assignment

    assert response.status_code == 400


def test_grade_assignment(client, h_principal):
    response = client.post(
        '/principal/assignments/grade',
        json={
            'id': 4,
            'grade': GradeEnum.C.value
        },
        headers=h_principal
    )

    assert response.status_code == 200

    assert response.json['data']['state'] == AssignmentStateEnum.GRADED.value
    assert response.json['data']['grade'] == GradeEnum.C


def test_regrade_assignment(client, h_principal):
    response = client.post(
        '/principal/assignments/grade',
        json={
            'id': 4,
            'grade': GradeEnum.B.value
        },
        headers=h_principal
    )

    assert response.status_code == 200

    assert response.json['data']['state'] == AssignmentStateEnum.GRADED.value
    assert response.json['data']['grade'] == GradeEnum.B
