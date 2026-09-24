class Solution:
    def earliestFinishTime(
        self,
        landStartTime: List[int],
        landDuration: List[int],
        waterStartTime: List[int],
        waterDuration: List[int]
    ) -> int:

        # used answer to store earliest finish time.
        answer = float("inf")

        # tried every land ride.
        for i in range(len(landStartTime)):

            # tried every water ride.
            for j in range(len(waterStartTime)):

                # calculated finish time of land ride.
                landFinish = landStartTime[i] + landDuration[i]

                # calculated actual start time of water ride.
                waterStart = max(waterStartTime[j], landFinish)

                # updated answer for land then water.
                answer = min(
                    answer,
                    waterStart + waterDuration[j]
                )

                # calculated finish time of water ride.
                waterFinish = waterStartTime[j] + waterDuration[j]

                # calculated actual start time of land ride.
                landStart = max(landStartTime[i], waterFinish)

                # updated answer for water then land.
                answer = min(
                    answer,
                    landStart + landDuration[i]
                )

        # returned earliest possible finish time.
        return answer