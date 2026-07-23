from client import ProactiveGoalDrivenAgentTeamClient

def main():
    client = ProactiveGoalDrivenAgentTeamClient()
    res = client.execute_team_goal(
        high_level_goal="Increase e-commerce store conversion rate by 15%",
        team_roles=["Data_Analyst", "Copywriter", "A/B_Test_Executor"]
    )
    print(f"Progress: {res['progress']}")
    print("Team Tasks:")
    for t in res["team_tasks"]:
        print(f"  [{t['agent_role']}] {t['assigned_subtask']} -> {t['status']}")

if __name__ == "__main__":
    main()
