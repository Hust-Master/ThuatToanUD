# import pandas as pd

# # Dữ liệu các câu hỏi
# questions_data = [
#     {
#         "stt": 1,
#         "cau_hoi": "Các gói công việc (work package) được mô tả trong:\na. Quy định công việc\nb. Bảng kê công việc\nc. Cấu trúc phân cấp công việc\nd. Kế hoạch dự án công việc",
#         "dap_an": "c. Cấu trúc phân cấp công việc",
#         "giai_thich": "Trong quản lý dự án, các gói công việc được mô tả chi tiết trong WBS (Work Breakdown Structure)."
#     },
#     {
#         "stt": 2,
#         "cau_hoi": "You work for a large manufacturing plant... To complete the Create WBS process sufficiently, you decide to do which of the following:\na. Elaborate the WBS to the point where the new machine specifications are clear and highly detailed.\nb. Record the code of account identifier, an SOW, responsible organization, and milestone schedule in the WBS dictionary for the components of the WBS.\nc. Use the organizational breakdown structure and the WBS together, and present this scope baseline to stakeholders.\nd. Record the approved change requests as one of the outputs of this process.",
#         "dap_an": "b. Record the code of account identifier, an SOW, responsible organization, and milestone schedule in the WBS dictionary for the components of the WBS.",
#         "giai_thich": "The WBS dictionary includes code of account, statement of work, responsible organization, milestones, etc., which is an output of Create WBS process. (WBS dictionary chứa mã tài khoản, SOW, tổ chức chịu trách nhiệm, các mốc, là đầu ra của quá trình Create WBS.)"
#     },
#     {
#         "stt": 3,
#         "cau_hoi": "Which of the following makes up the project scope baseline?\na. The scope management plan and WBS\nb. The project scope statement\nc. The WBS, project scope statement, and WBS dictionary\nd. The scope management plan, the WBS, and the WBS dictionary",
#         "dap_an": "c. The WBS, project scope statement, and WBS dictionary",
#         "giai_thich": "The scope baseline consists of the WBS, project scope statement, and WBS dictionary. (Phạm vi baseline gồm WBS, bản tuyên bố phạm vi dự án và từ điển WBS.)"
#     },
#     {
#         "stt": 4,
#         "cau_hoi": "Within your company’s portfolio, your project is ranked in the top five... To ensure that your target finish date does not slip in the critical chain method, you should:\na. Add a project buffer\nb. Determine the drum resource\nc. Put in three feeding buffers\nd. Manage the total float of the network paths",
#         "dap_an": "a. Add a project buffer",
#         "giai_thich": "In Critical Chain Method, adding a project buffer protects the target finish date. (Trong phương pháp Critical Chain, thêm project buffer giúp bảo vệ ngày hoàn thành dự án.)"
#     },
#     {
#         "stt": 5,
#         "cau_hoi": "You are working on a project that is similar in scope to a project performed last year by your company. You might consider which of the following:\na. Using the previous project’s WBS as a template\nb. Reusing the previous project’s cost-benefit analysis as justification for this project\nc. Reusing the previous project’s product description when writing the scope statement\nd. Using the previous project’s alternatives identification as a template",
#         "dap_an": "a. Using the previous project’s WBS as a template",
#         "giai_thich": "The WBS from a previous similar project can be reused as a template. (WBS từ dự án tương tự trước đó có thể tái sử dụng như một mẫu.)"
#     },
#     {
#         "stt": 6,
#         "cau_hoi": "Your approved project schedule was based on resource leveling... Which of the following methods will you use to recalculate the schedule?\na. Resource manipulation\nb. Resource reallocation\nc. Reverse resource allocation\nd. Critical chain scheduling",
#         "dap_an": "d. Critical chain scheduling",
#         "giai_thich": "Critical Chain Scheduling recalculates the schedule under resource constraints while minimizing project duration. (Critical Chain Scheduling tính toán lại lịch trình khi bị hạn chế tài nguyên để giảm tối đa thời gian dự án.)"
#     },
#     {
#         "stt": 7,
#         "cau_hoi": "All of the following are true regarding Communications Planning except for which one?\na. It’s the only output of the Communications Planning process.\nb. Communications requirements analysis, communications technology, and PMIS are tools and techniques of this process.\nc. It’s tightly linked with enterprise environmental factors and organizational influences, and lessons learned and historical information are two inputs that should get a lot of attention during this process.\nd. It should be completed as early in the project phases as possible.",
#         "dap_an": "a. It’s the only output of the Communications Planning process.",
#         "giai_thich": "This is incorrect; Communications Planning produces the Communications Management Plan but not only this. (Sai; Communications Planning tạo ra Communications Management Plan nhưng không chỉ có duy nhất output này.)"
#     },
#     {
#         "stt": 8,
#         "cau_hoi": "All of the following are true regarding stakeholder analysis except for which one?\na. It prioritizes and quantifies needs and wants to create project requirements.\nb. It determines communication needs and methods for updating stakeholders.\nc. It documents the needs, wants, and expectations of the stakeholders.\nd. It’s a tool and technique of the Scope Definition process.",
#         "dap_an": "d. It’s a tool and technique of the Scope Definition process.",
#         "giai_thich": "Stakeholder analysis is a tool of Identify Stakeholders process, not Scope Definition. (Stakeholder analysis là công cụ của Identify Stakeholders, không phải Scope Definition.)"
#     },
#     {
#         "stt": 9,
#         "cau_hoi": "Your project depends on a key deliverable from a vendor you’ve used several times before... This is an example of a/an\na. objective\nb. requirement\nc. constraint\nd. assumption",
#         "dap_an": "d. assumption",
#         "giai_thich": "Counting on a vendor deliverable is an assumption since it is believed to be true but not guaranteed. (Dựa vào việc nhà cung cấp giao hàng là assumption vì tin rằng sẽ đúng nhưng không đảm bảo.)"
#     },
#     {
#         "stt": 10,
#         "cau_hoi": "Nhóm các thành phần nào sau đây tham gia vào việc lập bảng công việc WBS ?\na. Người quản lý dự án, Khách hàng, thành viên tố dự án, người tài trợ\nb. Ban lãnh đạo, nhóm hỗ trợ, người tài trợ, người quản lý dự án\nc. Nhóm các chuyên môn, tổ dự án, khách hàng, Ban lãnh đạo\nd. Tổ dự án, Người tài trợ dự án, người quản lý dự án, người sử dụng",
#         "dap_an": "a. Người quản lý dự án, Khách hàng, thành viên tổ dự án, người tài trợ",
#         "giai_thich": "Các bên tham gia lập WBS gồm người quản lý dự án, khách hàng, thành viên dự án, và người tài trợ."
#     }
# ]

# # Tạo DataFrame
# df = pd.DataFrame(questions_data)

# # Xuất ra file Excel
# file_path = '/PMP_Study_Questions.xlsx'
# df.to_excel(file_path, index=False)
# file_path


arr = list(range(1, 3+1))

b = map(str, arr)
print('xxx', b)

a = ",".join(map(str, arr)) 

print(a)

print(";".join(['1', '2', '3']))