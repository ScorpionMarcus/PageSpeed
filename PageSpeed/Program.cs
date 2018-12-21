using System;
using System.Web;
using System.Net;
using System.IO;
using Newtonsoft.Json;

namespace PageSpeedApi
{
    class Program
    {
        static void Main(string[] args)
        {
            PageSpeed ps = new PageSpeed();

            Console.WriteLine("Enter domain: ");
            string url = Console.ReadLine();

            // https://www.googleapis.com/pagespeedonline/v4/runPagespeed?url=https%3a%2f%2fwww.performance-law.com&strategy=mobile&key=AIzaSyDJNu6pW7kifKiVssTdMlyad-hUc3stgOg

            string googlePageSpeedApiUrl = "https://www.googleapis.com/pagespeedonline/v4/runPagespeed";

            string pagespeedUrl = googlePageSpeedApiUrl +
            "?url=" + HttpUtility.UrlEncode(url) +
            "&strategy=mobile&key=" + ps.apiKey;

            string content = string.Empty;
            WebResponse response = null;
            WebRequest wr = WebRequest.Create(pagespeedUrl);
            wr.Method = "GET";
            response = wr.GetResponse();

            using (StreamReader sr = new StreamReader(response.GetResponseStream()))
            {
                content = sr.ReadToEnd();
                sr.Close();
            }

            //var json = JsonConvert.DeserializeObject<PageSpeedData>(content);

            //Console.WriteLine(content);
            Console.WriteLine(pagespeedUrl);
            Console.ReadLine();

        }
    }
}
